FROM openfabric/tee-python-cpu:latest

RUN mkdir application
WORKDIR /application
COPY . .

RUN poetry install -vvv --no-dev
RUN apt update && apt install -y git apt-utils

EXPOSE 5500

RUN pip3 uninstall -y openfabric-pysdk
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install transformers accelerate bitsandbytes>=0.39.0

CMD ["sh","start.sh"]