# directive = value

# create my image base on python3
FROM python:3

WORKDIR ~/

#add my python scipt to the docker file
ADD *.py ./
ADD Scores.txt ./

RUN pip install -r requrments.txt

#run my scipt on the default host
CMD [ "python3", "MainScores.py" ]

# Finalize application
EXPOSE 8777
