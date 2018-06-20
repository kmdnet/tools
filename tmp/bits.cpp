#include<Windows.h>
#include<stdio.h>

#include"bits.h"

int bits() {
	HRESULT hr;
	IBackgroundCopyManager* pIBackgroundCopyManager = NULL;
	GUID JobID;
	IBackgroundCopyJob* pJob;
	BG_JOB_STATE pJobState;

	
	hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
	if (SUCCEEDED(hr)) {
		hr = CoCreateInstance(__uuidof(BackgroundCopyManager), NULL, CLSCTX_LOCAL_SERVER, __uuidof(IBackgroundCopyManager), (LPVOID*)&pIBackgroundCopyManager);
		if (SUCCEEDED(hr)) {
			hr = pIBackgroundCopyManager->CreateJob(L"MyJob-Display", BG_JOB_TYPE_DOWNLOAD, &JobID, &pJob);
			if (SUCCEEDED(hr)) {
				hr = pJob->AddFile(L"http://127.0.0.1:8080/hoge.txt", L"C:\\work\\hoge.txt");
				if (SUCCEEDED(hr)) {
					hr = pJob->Resume();
					if (SUCCEEDED(hr)) {
						
						while (1) {
							hr = pJob->GetState(&pJobState);
							if (pJobState == BG_JOB_STATE_TRANSFERRED) {
								break;
							}
							Sleep(1000);
						}


						hr = pJob->Complete();
						if (SUCCEEDED(hr)) {
							printf("SUCCESS hr : 0x%x\n", hr);
						}

					}
					else {
						printf("pJob->Resume() : 0x%x\n", hr);
					}
				}
				else {
					printf("pJob->AddFile : 0x%x\n", hr);
				}
			}
			else {
				printf("pIBackgroundCopyManager->CreateJob : 0x%x\n", hr);
			}
		}
		else {
			printf("CoCreateInstance : 0x%x\n", hr);
		}
	}
	else {
		printf("CoInitializeEx : 0x%x\n", hr);
	}
	

	CoUninitialize();

	return 0;
}
