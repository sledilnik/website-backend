import io
import datetime

import pandas as pd
import pandas_schema.validation as validators
from pandas_schema import Column, Schema

from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import IntervalKind, Model, Prediction, PredictionData, Scenario


# -----------------------------------------------------------------------------
# Models

def model_to_json(model):
    return {
        "Id": model.id,
        "Name": model.name,
        "Www": model.www,
        "Description": model.description,
        "Contacts": [{"Name": contact.name, "Email": contact.email} for contact in model.contacts.all()]
    }


def scenario_to_json(scenario):
    return {
        "Id": scenario.id,
        "Slug": scenario.slug,
        "Name": scenario.name,
        "Description": scenario.description,
    }


def intervalKind_to_json(intervalKind):
    return {
        "Id": intervalKind.id,
        "Slug": intervalKind.slug,
        "Name": intervalKind.name,
        "Description": intervalKind.description,
    }


def prediction_to_json(prediction):
    return {
        "Date": prediction.date,
        "ModelId": prediction.model.id,
        "ScenarioId": prediction.scenario.id,
        "IntervalKindId": prediction.interval_kind.id,
    }


def models(request):

    return JsonResponse({
        "Models": [model_to_json(model) for model in Model.objects.filter(active=True)],
        "Scenarios": [scenario_to_json(scenario) for scenario in Scenario.objects.all()],
        "IntervalKinds": [intervalKind_to_json(intervalKind) for intervalKind in IntervalKind.objects.all()],
        "Predictions": [prediction_to_json(prediction) for prediction in Prediction.objects.all().order_by("date")]
    }, safe=False)


# -----------------------------------------------------------------------------
# Predictions

class PredictionForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={"placeholder": "YYYY-MM-DD"}))
    model = forms.ModelChoiceField(queryset=Model.objects.filter(active=True))
    password = forms.CharField(widget=forms.PasswordInput())
    scenario = forms.ChoiceField()
    interval_kind = forms.ChoiceField()
    data = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["scenario"].choices = [('', '---------')] + [(scenario.slug, scenario.name) for scenario in Scenario.objects.all()]
        self.fields["interval_kind"].choices = [('', '---------')] + [(interval_kind.slug, interval_kind.name) for interval_kind in IntervalKind.objects.all()]

    def clean(self):
        data = super().clean()

        if data.get("model") and data.get("password"):
            if data.get("model").password != data.get("password"):
                raise forms.ValidationError("Invalid credentials")

        if data.get("date") and not data.get("date").year >= 2020:
            self.add_error("scenario", "Invalid date year: {}.".data.get("date").year)

        if data.get("scenario") and not Scenario.objects.filter(slug=data["scenario"]).exists():
            self.add_error("scenario", "Scenario identified by the slug {} does not exist.".format(data["scenario"]))

        if data.get("interval_kind") and not IntervalKind.objects.filter(slug=data["interval_kind"]).exists():
            self.add_error("interval_kind", "IntervalKind identified by the slug {} does not exist.".format(data["interval_kind"]))

        def is_positive_int(x):
            try:
                return int(x) >= 0
            except ValueError:
                return False

        def is_positive_int_option(x):
            if pd.isna(x):
                return True
            else:
                try:
                    return int(x) >= 0
                except ValueError:
                    return False

        positiveIntValidator = validators.CustomElementValidation(is_positive_int, message="Expected positive int.")
        positiveIntOptionValidator = validators.CustomElementValidation(is_positive_int_option, message="Expected positive int or empty value.")

        prediction_data_schema = Schema([
            Column("date", [validators.DateFormatValidation("%Y-%m-%d"), validators.IsDistinctValidation()]),
            Column("hospitalized", [positiveIntValidator]),
            Column("hospitalizedLowerBound", [positiveIntOptionValidator]),
            Column("hospitalizedUpperBound", [positiveIntOptionValidator]),
            Column("icu", [positiveIntValidator]),
            Column("icuLowerBound", [positiveIntOptionValidator]),
            Column("icuUpperBound", [positiveIntOptionValidator]),
            Column("deceased", [positiveIntValidator]),
            Column("deceasedLowerBound", [positiveIntOptionValidator]),
            Column("deceasedUpperBound", [positiveIntOptionValidator]),
            Column("deceasedToDate", [positiveIntValidator]),
            Column("deceasedToDateLowerBound", [positiveIntOptionValidator]),
            Column("deceasedToDateUpperBound", [positiveIntOptionValidator]),
        ])

        if data.get("data"):
            prediction_data = pd.read_csv(io.StringIO(data.get("data").read().decode("utf-8")))
            data.get("data").seek(0)
            errors = prediction_data_schema.validate(prediction_data)
            if errors:
                for error in errors:
                    self.add_error("data", str(error))


@csrf_exempt
def predictions(request):
    form = PredictionForm(request.POST, request.FILES)

    if request.POST:
        if form.is_valid():
            prediction, created = Prediction.objects.get_or_create(
                date=form.cleaned_data["date"],
                model=form.cleaned_data["model"],
                scenario=Scenario.objects.get(slug=form.cleaned_data["scenario"]),
                interval_kind=IntervalKind.objects.get(slug=form.cleaned_data["interval_kind"]),
            )

            if not created:
                prediction.data.all().delete()

            data = pd.read_csv(io.StringIO(form.cleaned_data["data"].read().decode("utf-8")))

            for index, row in data.iterrows():
                PredictionData.objects.create(
                    date=row["date"],
                    prediction=prediction,
                    hospitalized=row["hospitalized"],
                    hospitalizedLowerBound=row["hospitalizedLowerBound"],
                    hospitalizedUpperBound=row["hospitalizedUpperBound"],
                    icu=row["icu"],
                    icuLowerBound=row["icuLowerBound"],
                    icuUpperBound=row["icuUpperBound"],
                    deceased=row["deceased"],
                    deceasedLowerBound=row["deceasedLowerBound"],
                    deceasedUpperBound=row["deceasedUpperBound"],
                    deceasedToDate=row["deceasedToDate"],
                    deceasedToDateLowerBound=row["deceasedToDateLowerBound"],
                    deceasedToDateUpperBound=row["deceasedToDateUpperBound"],
                )

            return JsonResponse({
                "prediction": {
                    "id": prediction.id,
                    "status": "created" if created else "updated"
                }
            })
        else:
            return JsonResponse({"error": form.errors}, status=400)
    else:
        form = PredictionForm()

    return render(request, "modeling/prediction.html", {
        "form": form
    })


# -----------------------------------------------------------------------------
# Predictions data

def predictionData_to_json(predictionData):
    return {
        "Date": predictionData.date.strftime("%Y-%m-%d"),
        "PredictionId": predictionData.prediction.id,
        "Icu": predictionData.icu,
        "IcuLowerBound": predictionData.icuLowerBound,
        "IcuUpperBound": predictionData.icuUpperBound,
        "Hospitalized": predictionData.hospitalized,
        "HospitalizedLowerBound": predictionData.hospitalizedLowerBound,
        "HospitalizedUpperBound": predictionData.hospitalizedUpperBound,
        "Deceased": predictionData.deceased,
        "DeceasedLowerBound": predictionData.deceasedLowerBound,
        "DeceasedUpperBound": predictionData.deceasedUpperBound,
        "DeceasedToDate": predictionData.deceasedToDate,
        "DeceasedToDateLowerBound": predictionData.deceasedToDateLowerBound,
        "DeceasedToDateUpperBound": predictionData.deceasedToDateUpperBound,
    }


def predictions_data_for_date(request, year, month, day):
    try:
        date = datetime.date(year=year, month=month, day=day)
    except ValueError:
        return JsonResponse({"error": "Invalid date: {}-{}-{}".format(year, month, day)})

    return JsonResponse(
        [predictionData_to_json(predictionData)
         for predictionData
         in PredictionData.objects.filter(prediction__date=date).order_by("date")], safe=False)
