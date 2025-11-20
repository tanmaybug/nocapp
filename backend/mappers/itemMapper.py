from dtos.itemDTO import ItemResponseDTO

def dbtodto(data):
    item = ItemResponseDTO(
        test_id=data.test_id, sname=data.name, phone=data.phone, email=data.email
    )
    return item

def dbtodtolist(data):
    y = []
    for x in data:
        y.append(ItemResponseDTO(**x))
    return y