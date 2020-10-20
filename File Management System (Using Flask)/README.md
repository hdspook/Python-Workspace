File Management Application

-> Apis
1) "/retriev" -> Post Request
	Usage -> url = "http://127.0.0.1:5000/retrieve"
		 x = requests.post(url, data = {'file' : 'test.txt'})

2) "/convert" -> Post Requet
	Usage -> url = "http://127.0.0.1:5000/convert"
		 x = requests.post(url, data = {'file' : 'Dummy.docx'})

3) "/merge" -> Post Requet
	Usage -> url = "http://127.0.0.1:5000/merge"
		 x = requests.post(url, data = {'file' : 'Dummy.pdf,b_2.pdf'})
			
	Accepts a list of pdfs.
