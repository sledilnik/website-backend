import datetime
from django.http import JsonResponse

from .models import Model, Scenario, IntervalKind, Prediction, PredictionData


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


def predictions_data(request, year, month, day):
    try:
        date = datetime.date(year=year, month=month, day=day)
    except ValueError:
        return JsonResponse({"error": "Invalid date: {}-{}-{}".format(year, month, day)})

    return JsonResponse([
        predictionData_to_json(predictionData)
        for predictionData
        in PredictionData.objects.filter(prediction__date=date).order_by("date")],
        safe=False)
