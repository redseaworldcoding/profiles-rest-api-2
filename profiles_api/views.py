# Import APIView class from the rest_framework.views modules
from rest_framework.views import APIView

# Imports the response object which used to return responses from the APIView
from rest_framework.response import Response

# Create new class based on the APIView class.
class HelloApiView(APIView):
    """Test API View"""

    # Handles HTTP Get Request where it calls get function....
    def get(self, request, format=None):
        """Returns a list of APIView features"""

        # DEfine a list which describes all of the features of an APIView:

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View'
            'Gives you the most control over your application logic'
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
