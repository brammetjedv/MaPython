import math

appelbomen = 333
appelbomenInZon = appelbomen / 3
appelbomenInNietZon = appelbomenInZon * 2
appelsPerZonBoom = 146
appelsPerNietZonBoom = (appelsPerZonBoom / 100) * 80
appels = (appelsPerZonBoom + appelsPerNietZonBoom) * appelbomen
verkoopbareAppels = appels / 3


print(math.floor(verkoopbareAppels))
