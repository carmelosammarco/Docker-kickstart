FROM ubuntu:latest

LABEL maintainer="Carmelo Sammarco <carmelosammarco.com>"

#To make the installation not interactive 
ARG DEBIAN_FRONTEND=noninteractive


#Install miniconda
RUN apt-get -qq update && apt-get -qq -y install --no-install-recommends  ca-certificates curl  bzip2 \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes

#Create an environment path where miniconda python distribution can be found
ENV PATH /opt/conda/bin:$PATH

#Copy data folder to the image
RUN mkdir SRC
WORKDIR /SRC
COPY . .

#Create python environment
RUN conda env create -n myenv -f environment.yml

#Make RUN commands use the new python environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

#Port to expose
EXPOSE 8888

#Select the working directory
WORKDIR /SRC/Notebook

#Start the jupiter-lab session
ENTRYPOINT ["conda", "run", "-n", "myenv", "jupyter", "lab",  "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token='sicilian4ever'", "--NotebookApp.password='sicilian4ever'"]

#If you want remove login credentials add to the command above the following:
#"--NotebookApp.token=''", "--NotebookApp.password=''"
