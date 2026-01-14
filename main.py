import json
from datetime import datetime

class AIContentPipeline:
    def __init__(self, project_name):
        self.project_name = project_name

    def generate(self, request):
        return {
            "project": self.project_name,
            "content_type": request["content_type"],
            "style": request["style"],
            "character": request.get("character", {}),
            "constraints": request.get("constraints", []),
            "generated_at": datetime.now().isoformat(),
            "result": f"{request['content_type']} generated for character {request.get('character', {}).get('name', 'N/A')}."
        }


pipeline = AIContentPipeline("Structured AI Workflow for Consistent Content Creation")

request = {
    "content_type": "AI Influencer Caption",
    "style": "Luxury Retro Digital",
    "character": {
        "name": "AVA",
        "personality": "Confident, bold, aspirational",
        "tone": "High-end editorial"
    },
    "constraints": [
        "Persona consistency",
        "Luxury vocabulary",
        "Scalable format"
    ]
}

output = pipeline.generate(request)

print(json.dumps(output, indent=4))
