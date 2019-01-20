# Takes image url and gives the word for what it is
import sys
import json
from watson_developer_cloud import VisualRecognitionV3
from building.getwikipediaarticle import WikiPage
"""
Input the url link of a picture and getWord will return the best classifier word
for what the picture shows.
"""


def getWord(url):
    visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey='G_vhnFiNCnhp97Uew544e5aF0NfcNzkL-FRWcZ-L_uAq')

    classes_result = visual_recognition.classify(url=url).get_result()
    image = json.dumps(classes_result, indent=2)
    return image.splitlines()[9].strip()[10:-2]
    # ['images'][0]['classifiers'][0]['classes'][0]['class']


if __name__ == "__main__":
    word = getWord(sys.argv[1])
    page = WikiPage(word)