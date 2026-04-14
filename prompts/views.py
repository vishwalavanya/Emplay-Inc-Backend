import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Prompt


@csrf_exempt
def prompts_handler(request):
    if request.method == "GET":
        prompts = Prompt.objects.all()
        data = [p.to_dict() for p in prompts]
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)

            title = data.get("title")
            content = data.get("content")
            complexity = data.get("complexity")
            tags = data.get("tags", [])   # ✅ IMPORTANT

            # validations
            if not title or len(title) < 3:
                return JsonResponse({"error": "Title too short"}, status=400)

            if not content or len(content) < 10:
                return JsonResponse({"error": "Content too short"}, status=400)

            if not (1 <= int(complexity) <= 10):
                return JsonResponse({"error": "Invalid complexity"}, status=400)

            # ✅ SAVE TAGS HERE
            prompt = Prompt.objects.create(
                title=title,
                content=content,
                complexity=complexity,
                tags=tags
            )

            return JsonResponse({
                "message": "Prompt created",
                "id": str(prompt.id)
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


def get_prompt_detail(request, id):
    try:
        prompt = Prompt.objects.get(id=id)

        # simple view count logic
        view_count = getattr(prompt, "_view_count", 0) + 1
        prompt._view_count = view_count

        return JsonResponse(prompt.to_dict(view_count=view_count))

    except Prompt.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
