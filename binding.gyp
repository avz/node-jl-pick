{
	"targets": [
		{
			"target_name": "jl-pick",
			"sources": [],
			"dependencies": ["make"]
		},
		{
			"target_name": "make",
			"actions": [
				{
					"action_name": "make",
					"inputs": ["native/Makefile"],
					"outputs": ["native/bin/jl-pick"],
					"action": ["make", "-C", "native"],
					"message": "Build jl-pick"
				}
			]
		}
	]
}
