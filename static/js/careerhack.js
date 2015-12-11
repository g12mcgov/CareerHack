/* 
* @Author: grantmcgovern
* @Date:   2015-12-10 16:36:40
* @Last Modified by:   grantmcgovern
* @Last Modified time: 2015-12-11 00:50:53
*/

$(document).ready(function() {
	// Add question button handler
	$("#add-question").on('click', function(event) {
		// Display modal to add question
		$("#add-question-modal").modal('show');
	});

	// Process add question form submission
	$("#add-question-form-button").on('click', function(event) {
		event.preventDefault();
		var company_name = $('.questions').data('company-name');
		// POST data
		var data = {
			'interviewer_input': $('#interviewer-input').val(),
			'question_input': $('#question-input').val(),
			'answer_input': $('#answer-input').val(),
			'position_input': $('#question-input')
		};
		console.log(data);
		// Ajax request for form submission
		$.ajax({
			url: '/insert-question/' + company_name,
			type: 'POST',
			dataType: 'JSON',
			data: JSON.stringify(data),
			success: function(data) {

			},
			error: function(error) {
				console.log(error);
			}
		});
		$("#add-question-modal").modal('hide');
	});
});
