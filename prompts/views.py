import json
import redis
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from .models import Prompt

load_dotenv()

# ✅ Redis connection (safe)
try:
    r = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True
    )
    r.ping()
except:
    r = None


# ✅ GET + POST handler
@csrf_exempt
def prompts_handler(request):

    # 🔹 GET → list all prompts
    if request.method == "GET":
        prompts = list(Prompt.objects.values())
        return JsonResponse(prompts, safe=False)

    # 🔹 POST → create prompt
    elif request.method == "POST":
        try:
            data = json.loads(request.body)

            title = data.get("title")
            content = data.get("content")
            complexity = data.get("complexity")

            # ✅ validation
            if not title or len(title) < 3:
                return JsonResponse({"error": "Title must be at least 3 chars"}, status=400)

            if not content or len(content) < 20:
                return JsonResponse({"error": "Content must be at least 20 chars"}, status=400)

            if not (1 <= int(complexity) <= 10):
                return JsonResponse({"error": "Complexity must be 1-10"}, status=400)

            prompt = Prompt.objects.create(
                title=title,
                content=content,
                complexity=complexity
            )

            return JsonResponse({
                "message": "Prompt created",
                "id": prompt.id
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


# ✅ GET single prompt (with Redis view count)
def get_prompt_detail(request, id):
    try:
        prompt = Prompt.objects.get(id=id)

        # Redis key
        key = f"prompt:{id}:views"

        if r:
            views = r.incr(key)
        else:
            views = 1  # fallback if Redis not running

        return JsonResponse({
            "id": prompt.id,
            "title": prompt.title,
            "content": prompt.content,
            "complexity": prompt.complexity,
            "created_at": prompt.created_at,
            "view_count": views
        })

    except Prompt.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)