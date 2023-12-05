def transcode(input_file,output_file):
    import json

    status = 'OK'

    try:
        with open(input_file, encoding='utf-8-sig') as fh:
            content = json.load(fh)  # Read JSON content directly using json.load()
    except Exception as e:
        status = str(e)
        print(status)
        return status  # Return here if an exception occurred

    print("------------------------")
    print("")
   
    decoded_content = bytes((json.dumps(content,ensure_ascii=False)), encoding='utf-8').decode('unicode_escape')
    decoded_content = json.dumps(content,ensure_ascii=False)
    
    print(type(decoded_content))
    print("------------------------")
    
    decoded_content_json = json.loads(decoded_content)
    
    print("------------------------")
    with open(output_file, "w",encoding='utf-8-sig') as out:
        # out.write(decoded_content)
        json.dump(decoded_content_json['items'], out, indent=2,ensure_ascii=False)  
    return status

transformJsonForSasMap(r"\\edw-sas-t-cx-01\Test\External\EMT\Python_Scripts\response\DataHub_Test_EmtRaw.json")
