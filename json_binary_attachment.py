import base64
import json

path = r"//pi9995-FS01.intern.sdc.dk/PI9995-01$/Homedir/T7430/Dokumenter/Docs/DEV/S199/1195287 CRD V OP Risk Spike Story Data from LinkGRC-API into EDW/python/resp_9961.json"

f=open(path)
data=json.load(f)

# DOCX
doc_name=data['Details'][0]['Document-Data'][0]['name']
outfile = r"//pi9995-FS01.intern.sdc.dk/PI9995-01$/Homedir/T7430/Dokumenter/Docs/DEV/S199/1195287 CRD V OP Risk Spike Story Data from LinkGRC-API into EDW/python/"+doc_name
doc_content_enc=data['Details'][0]['Document-Data'][0]['dataStream']



# JPEG
# doc_name       =data['Details'][15]['Attachment-Data'][0]['FileName']
# outfile = r"//pi9995-FS01.intern.sdc.dk/PI9995-01$/Homedir/T7430/Dokumenter/Docs/DEV/S199/1195287 CRD V OP Risk Spike Story Data from LinkGRC-API into EDW/python/"+doc_name+".jpg"
# doc_content_enc=data['Details'][15]['Attachment-Data'][0]['DataStream']

# f_word = open(outfile, "a")

with open(outfile, "wb") as new_file:
    # new_file.write(base64.decodebytes(doc_content_enc))
    new_file.write(base64.urlsafe_b64decode(doc_content_enc))

new_file.close()

f.close()
