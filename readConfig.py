import yaml

with open("productTypes.yaml", 'r', encoding="utf-8") as productTypesYaml:
    productTypes = yaml.load(productTypesYaml)
	
for productType in productTypes:
	print(productType)
	for identifier in productTypes[productType]:
		print(identifier)