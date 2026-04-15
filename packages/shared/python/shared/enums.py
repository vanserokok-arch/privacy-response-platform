import enum


class Jurisdiction(str, enum.Enum):
    ru = "RU"
    kz = "KZ"
    by = "BY"
    ua = "UA"


class SearchProvider(str, enum.Enum):
    yandex = "yandex"
    google = "google"
    vk = "vk"
    telegram = "telegram"

