
def definitions():
    # some abstraction
    DELIMITER=","
    global fields   
    fields={"housetype"	:	"classified.type",
    "subtype"	:	"classified.subtype",
    "price"	:	"classified.price",
    "transactionType"	:	"classified.transactionType",
    "zipcode"	:	"classified.zip",
    "kitchen"	:	"classified.kitchen.type",
    "constructionYear"	:	"classified.building.constructionYear",
    "buildingcondition"	:	"classified.building.condition",
    "conditionheatingType"	:	"classified.energy.heatingType",
    "EnergyConsumptionLevel"	:	"classified.certificates.primaryEnergyConsumptionLevel",
    "bedroomcount"	:	"classified.bedroom.count",
    "landsurface"	:	"classified.land.surface",
    "atticExists"	:	"classified.atticExists",
    "basementExists"	:	"classified.basementExists",
    "gardensurface"	:	"classified.outdoor.garden.surface",
    "terraceexists"	:	"classified.outdoor.terrace.exists",
    "SMEofficeexists"	:	"classified.specificities.SME.office.exists",
    "hasSwimmingPool"	:	"classified.wellnessEquipment.hasSwimmingPool",
    "parkingSpaceCountindoor"	:	"classified.parking.parkingSpaceCount.indoor",
    "parkingSpaceCountoutdoor"	:	"classified.parking.parkingSpaceCount.outdoor",
    "conditionNew"	:	"classified.condition.isNewlyBuilt",
    "customername"	:	"customer.name",
    "customerfamily"	:	"customer.family"
    }
