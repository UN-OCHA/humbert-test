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

RUN sed -i 's/self.RESULTS_DIR, "classification"/results_dir, "classification"/' /usr/local/lib/python3.11/dist-packages/classifier_trainer/main.py
RUN sed -i 's/save_results: bool = True,/save_results: bool = True,\n        results_dir: str = "results",/' /usr/local/lib/python3.11/dist-packages/classifier_trainer/main.py
RUN sed -i 's/file_name = f"classification_results_{self.results_name}.csv"/file_name = f"classification_results.csv"/' /usr/local/lib/python3.11/dist-packages/classifier_trainer/main.py

WORKDIR /workspace

CMD ["/bin/bash"]