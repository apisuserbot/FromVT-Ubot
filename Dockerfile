# We're using Ubuntu 20.10
FROM vckyouuu/kepoolow:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b FromVT-Ubot https://github.com/vckyou/FromVT-Ubot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/vckyou/FromVT-Ubot/FromVT-Ubot/requirements.txt

CMD ["python3","-m","userbot"]
