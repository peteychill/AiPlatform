import os
from dotenv import load_dotenv
from openai import OpenAI
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from django.http import JsonResponse
from .permissions import IsAllowedClient

# Load environment variables
load_dotenv()
apiKey = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=apiKey)

@api_view(['POST'])
@authentication_classes([OAuth2Authentication])
@permission_classes([IsAllowedClient])
def generate_text(request):
    # Check if the method is POST
    if request.method == "POST":
        data = request.data
        prompt = data.get("prompt", "")

        try:
            # Call OpenAI API for text generation
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            # Get the content from the response
            content = response.choices[0].message.content
            return JsonResponse({"response": content})
        except Exception as e:
            # Return error message if there's an issue
            return JsonResponse({"error": str(e)}, status=500)

    # If not a POST request, return an error
    return JsonResponse({"error": "POST only"}, status=400)
