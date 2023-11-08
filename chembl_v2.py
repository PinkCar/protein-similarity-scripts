import asyncio
import aiohttp
import time

filename = 'enh.txt' # change this to your file name!

async def submit_chembl_job(key, value):
    data = {"sequence": value,
            "dl__ignore_cache": "true",
            "exp": "1e-5",
        }
    url = "https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/submit/biological_sequence_search_job"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            job_id = (await response.json())["job_id"]
    return value, job_id

async def check_job_status(job_id):
    async with aiohttp.ClientSession() as session:
        url = "https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/status/{}".format(job_id)
        async with session.get(url, ssl=False) as response:
            job_status = (await response.json(content_type=None))["status"]
            log = (await response.json(content_type=None))["status_log"]
    return job_status, log

async def download_chembl_job_results(job_id):
    async with aiohttp.ClientSession() as session:
        url = "https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/outputs/{}/results.json".format(job_id)
        async with session.get(url) as response:
            search_results = (await response.json())["search_results"]
    return search_results

async def main():
    with open(filename, 'r') as f:
        enh_list = f.read().split('\n\n')
        enh_dict = {enh.split('\n')[0]: enh.split('\n')[1] for enh in enh_list}
    
    tasks = []
    for key, value in enh_dict.items():
        task = asyncio.create_task(submit_chembl_job(key, value))
        tasks.append(task)
    job_ids = await asyncio.gather(*tasks)

    enh_dict = dict(zip(enh_dict.keys(), job_ids))

    # Poll the ChEMBL API to check the status of the job.
    while enh_dict.items():
        if not enh_dict.items():
            break
        for seq in list(enh_dict.keys()):
            job_status, status_log = await check_job_status(enh_dict[seq][1])
            # print(job_status)
            if job_status == "FINISHED" or "Results Loaded!!!" in status_log:
                search_results = await download_chembl_job_results(enh_dict[seq][1])
                if search_results == []:
                    print(f"{seq} is not in ChemBL")
                else:
                    print(f"{seq} is in ChemBL")
                enh_dict.pop(seq)

                if not enh_dict.items():
                    print("All done!")
                    break
                print(len(enh_dict), "sequences left. Please wait...")
            elif job_status == "ERROR":
                raise Exception("ChEMBL job failed.")
            else:
                # print("check id", enh_dict[seq][1], "again in 1 second")
                time.sleep(1)

        


if __name__ == '__main__':
    asyncio.run(main())