$(document).ready(function(){
	
	var _DEFAULTS = {
		'wating' : 'Olá, estou esperando seu comando :)',
		'unsupported_browser': '<div class="alert alert-danger">Este navegador não é compatível com a Luna</div>',
		'processing' : '<i class="opacity-75">ouvindo e processando seu comando <i class="fa fa-spin fa-circle-o-notch" aria-hidden="true"></i></i>',
		'not_undesrtood' : 'Ops, houve uma falha... pode repetir, por favor?',
	}

	$status = $('#status-msg');
	$status.html((('webkitSpeechRecognition' in window)) ? _DEFAULTS['wating'] : _DEFAULTS['unsupported_browser']);

	var speechRecognition = new webkitSpeechRecognition();
	speechRecognition.continuous = true;
	speechRecognition.interimResults = true;
	speechRecognition.lang = "pt-BR";

	speechRecognition.onresult = function(e){
		var result = e.results[e.resultIndex];
		if (result.isFinal) {
			$status.html((result[0].transcript != '') ? '"'+result[0].transcript+'"' : _DEFAULTS['wating']);
		} else {
			$status.html(_DEFAULTS['processing']);
		}
	}

	speechRecognition.onerror = function(){
		$status.html(_DEFAULTS['not_undesrtood']);
	}

	speechRecognition.start();

});