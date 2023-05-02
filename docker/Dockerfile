FROM ubuntu:23.04
LABEL maintainer="Hugging Face"
LABEL repository="transformers"

RUN apt update && \
    apt install -y bash \
                   build-essential \
                   git \
                   curl \
                   ca-certificates \
                   python3 \
                   python3-pip && \
    rm -rf /var/lib/apt/lists

RUN python3 -m pip install --break-system-packages --no-cache-dir --upgrade pip && \
    python3 -m pip install --break-system-packages --no-cache-dir jupyter matplotlib && \
    python3 -m pip install --break-system-packages git+https://github.com/the-deep-nlp/classifier-trainer

RUN python3 -m pip install --break-system-packages --no-cache-dir seaborn

WORKDIR /workspace

CMD ["/bin/bash"]