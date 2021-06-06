from .test_setup import TestSetUp
import json

class TestViews(TestSetUp):
    # happy flow
    def test_user_can_register_correctly(self):
        res=self.client.post(self.registerUrl,self.user_data,format="json")
        self.assertEqual(res.status_code,201)

    def test_file_can_login_correctly(self):
        # register user
        res=self.client.post(self.registerUrl,self.user_data,format="json")
        # test login
        res=self.client.post(self.loginUrl,self.user_data,format="json")
        self.assertEqual(res.status_code,200)

    def test_file_can_upload_correctly(self):
        # token authentication
        res=self.client.post(self.registerUrl,self.user_data,format="json")
        AuthToken=json.loads(res.content)['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + AuthToken)
        # test upload with positive file
        with open(self.posFile) as fp:
            res=self.client.post(self.uploadUrl, {'file': fp})
        self.assertEqual(res.status_code,200)

    def test_file_cant_upload_with_wrong_ext(self):
        # token authentication
        res=self.client.post(self.registerUrl,self.user_data,format="json")
        AuthToken=json.loads(res.content)['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + AuthToken)
        # test upload with negative file
        with open(self.negFile) as fp:
            res=self.client.post(self.uploadUrl, {'file': fp})
        self.assertEqual(res.status_code,400)

    def test_can_list_files_correctly(self):
        # token authentication
        res=self.client.post(self.registerUrl,self.user_data,format="json")
        AuthToken=json.loads(res.content)['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + AuthToken)
        # upload one file
        with open(self.posFile) as fp:
            res=self.client.post(self.uploadUrl, {'file': fp})
        # test get request to list 
        res=self.client.get(self.listUrl)
        self.assertEqual(res.status_code,200)

    # negative tests
    def test_user_cant_register_with_no_data(self):
        res=self.client.post(self.registerUrl)
        self.assertEqual(res.status_code,400)

    def test_file_cant_upload_without_authentication(self):
        # token authentication
        res=self.client.post(self.registerUrl,self.user_data,format="json")
        # AuthToken=json.loads(res.content)['token']
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + AuthToken)
        # test upload with positive file
        with open(self.posFile) as fp:
            res=self.client.post(self.uploadUrl, {'file': fp})
        self.assertEqual(res.status_code,401)

    def test_cant_list_files_with_wrong_token(self):
        # token authentication
        res=self.client.post(self.registerUrl,self.user_data,format="json")
        AuthToken=json.loads(res.content)['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + AuthToken)
        # upload one file
        with open(self.posFile) as fp:
            res=self.client.post(self.uploadUrl, {'file': fp})
        # spoil token
        self.client.credentials(HTTP_AUTHORIZATION='Token THIS_IS_A_SPOILT_TOKEN')
        # test get request to list 
        res=self.client.get(self.listUrl)
        self.assertEqual(res.status_code,401)