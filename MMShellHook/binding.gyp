{
	"targets": [
		{
			"target_name": "binding",
			"dependencies": [
				"keylistener"
			]
		},
		{
			"target_name": "keylistener",
			"type": "executable",
			"sources": [
				"win.cpp"
			],
	      'msvs_settings': {
	        'VCLinkerTool': {
	          'SubSystem': '1',
	          'EntryPointSymbol': 'mainCRTStartup',
	          'AdditionalDependencies': [
	              'user32.lib',
	          ],
	        },
	        }
		}
	]
}
