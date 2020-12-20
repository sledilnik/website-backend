FROM python:3.8

ARG USERNAME=vscode

ADD ./docker/setup.sh /setup.sh
RUN /setup.sh --dev && rm /setup.sh

USER ${USERNAME}
ENV PATH=/home/${USERNAME}/.local/bin:${PATH}