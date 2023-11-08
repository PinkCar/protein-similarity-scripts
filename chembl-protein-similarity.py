# read file from enh.txt
import requests
import time 

filename = 'enh.txt' # change this to your file name!

with open(filename, 'r') as f:
    enh_list = f.read().split('\n\n')
    enh_dict = {enh.split('\n')[0]: enh.split('\n')[1]for enh in enh_list}
    
    for key, value in enh_dict.items():
        data = {"sequence": value,
                "dl__ignore_cache": "true",
                "exp": "1e-5",
        }
        url = "https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/submit/biological_sequence_search_job"
        response = requests.post(url, data=data)
        job_id = response.json()["job_id"]


        # Poll the ChEMBL API to check the status of the job.
        while True:
            url = "https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/status/{}".format(job_id)
            response = requests.get(url)
            job_status = response.json()["status"]

            if job_status == "FINISHED":
                break
            elif job_status == "failed":
                raise Exception("ChEMBL job failed.")
            else:
                time.sleep(1)

        # Download the results.
        url = "https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/outputs/{}/results.json".format(job_id)
        response = requests.get(url)
        search_results = response.json()["search_results"]
        
        if search_results == []:
            print(f"{key} is not in ChemBL")
        else:
            print(f"{key} is in ChemBL")

