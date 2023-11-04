FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas numpy seaborn matplotlib scikit-learn scipy


RUN mkdir -p /home/doc-bd-a1/

COPY forbes_2640_billionaires.csv /home/doc-bd-a1/


COPY load.py dpre.py eda.py vis.py model.py final.sh /home/doc-bd-a1/

CMD ["bash"]

