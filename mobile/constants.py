from django.conf import settings

LEVEL_DRINK_MAP = {
    0:"Shamrock",
    1:"Shamrock Cow",
    2:"Shamrock Sheep",
    3:"Bar of Gold",
    4:"Pot of Gold",
    5:"Leprechaun Duck",
    6:"Leprechaun",
}

LEVEL_IMAGE_MAP = {
    0:"%simg/shamrock1.png" % settings.STATIC_URL,
    1:"%simg/shamrockcow2.png" % settings.STATIC_URL,
    2:"%simg/shamrocksheep3.png" % settings.STATIC_URL,
    3:"%simg/barofgold4.png" % settings.STATIC_URL,
    4:"%simg/potofgold5.png" % settings.STATIC_URL,
    5:"%simg/leprechaunduck6.png" % settings.STATIC_URL,
    6:"%simg/leprechaun7.png" % settings.STATIC_URL,
}
