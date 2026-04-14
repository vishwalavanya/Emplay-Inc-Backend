import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Prompt
import redis
from django.conf import settings

# Redis connection
try:
    redis_client = redis.from_url(settings.REDIS_URL)
except:
    redis_client = None


@csrf_exempt
def prompts_handler(request):
    if request.method == "GET":
        prompts = Prompt.objects.all()
        data = []

        for p in prompts:
            view_count = 0

            # 🔥 GET FROM REDIS
            if redis_client:
                try:
                    view_count = int(redis_client.get(f"prompt:{p.id}:views") or 0)
                except:
                    view_count = 0

            item = p.to_dict()
            item["view_count"] = view_count   # ✅ ADD THIS

            data.append(item)

        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)

            title = data.get("title")
            content = data.get("content")
            complexity = data.get("complexity")
            tags = data.get("tags", [])

            if not title or len(title) < 3:
                return JsonResponse({"error": "Title too short"}, status=400)

            if not content or len(content) < 10:
                return JsonResponse({"error": "Content too short"}, status=400)

            if not (1 <= int(complexity) <= 10):
                return JsonResponse({"error": "Invalid complexity"}, status=400)

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

        view_count = 0

        if redis_client:
            try:
                view_count = redis_client.incr(f"prompt:{id}:views")
            except:
                view_count = 0

        return JsonResponse(prompt.to_dict(view_count=view_count))

    except Prompt.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
