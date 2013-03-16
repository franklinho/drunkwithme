from django.conf import settings

LEVEL_CHOICES = (
    (0,"leprochon"),
)

LEVEL_DRINK_MAP = {
    0,"shamrock",
    1,"shamrock cow",
    2,"shamrock sheep",
    3,"bar of gold",
    4,"pot of gold",
    5,"leprechaun duck",
    6,"leprechaun",
}

LEVEL_IMAGE_MAP = {
    0,"%simg/shamrock1.png" % settings.STATIC_URL,
    1,"%simg/shamrockcow2.png" % settings.STATIC_URL,
    2,"%simg/shamrocksheep3.png" % settings.STATIC_URL,
    3,"%sbarofgold4.png" % settings.STATIC_URL,
    4,"%spotofgold5.png" % settings.STATIC_URL,
    5,"%sleprechaunduck6.png" % settings.STATIC_URL,
    6,"%sleprechaun7.png" % settings.STATIC_URL,
}
