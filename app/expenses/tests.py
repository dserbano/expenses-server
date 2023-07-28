from django.test import TestCase

# Create your tests here.

class RoutesTest(TestCase):
    

    #checking is route '/' exists
    def testAllExpenses(self):
        response = self.client.get('/')
        print(response)
        self.assertEqual(response.status_code, 200)