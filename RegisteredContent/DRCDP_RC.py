import json

source_id = {}
source_id['source_id'] = {}
RCs = ['source_id','institution_id','region']
inst_ids = []
keys = []

key = 'LOCA2'
keys.append(key)
source_id['source_id'][key] = {}
source_id['source_id'][key]['source_name'] = 'LOCA'
source_id['source_id'][key]['source_version_number'] = '2'
source_id['source_id'][key]['institution_id'] = 'UCSD-SIO'
source_id['source_id'][key]['region'] = ['north_america']

key = 'LOCA2.1'
keys.append(key)
source_id['source_id'][key] = {}
source_id['source_id'][key]['source_name'] = 'LOCA'
source_id['source_id'][key]['source_version_number'] = '2.1'
source_id['source_id'][key]['institution_id'] = 'UCSD-SIO'
source_id['source_id'][key]['region'] = ['north_america']

key = 'STAR-ESDM-v1'
keys.append(key)
source_id['source_id'][key] = {}
source_id['source_id'][key]['source_name'] = 'STAR-ESDM'
source_id['source_id'][key]['source_version_number'] = 'v1'
source_id['source_id'][key]['institution_id'] = 'TTU'
source_id['source_id'][key]['region'] = ['north_america']

for k in keys:
  inst = source_id['source_id'][k]['institution_id']
  if inst not in inst_ids:  inst_ids.append(inst)

for RC in RCS:
# Serializing json
 json_object = json.dumps(source_id, indent=4)
 
# Writing to sample.json
 with open("source_ids.json", "w") as outfile:
    outfile.write(json_object)


