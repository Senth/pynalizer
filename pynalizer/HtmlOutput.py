def _generate_head(participants):
    html = '<!DOCTYPE html><html><head><title>Conversation: '
    for participant in participants:
        html += participant.name + ', '
    html += '</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><table><tr>'
    return html

def _generate_foot():
    return '</body></html>'      

def _generate_participant(participant):
    html = '<td style="vertical-align: top; margin: 10px;">'
    html += '<h1>' + participant.name + '</h1>'
    html += '<table><tr><th style="text-align: left; padding: 2px;">Percent</th><th style="text-align: left; padding: 2px;">Count</th><th style="text-align: left; padding: 2px;">Word</th></tr>'

    max_count = -1

    for word_count in participant.get_sorted_word_list():
        word, count = word_count
        if max_count == -1:
            max_count = count
        if count < 10:
            break
        percent = count / max_count * 100.0
        percent_string = "{0:.2f}".format(percent)
        html += '<tr><td style="padding: 2px;">' + percent_string + ' %</td><td style="padding: 2px;">' + str(count) + '</td><td style="padding: 2px;">' + word + '</td></tr>'

    html += '</table></td>'
    return html

def generate_html(participants):
    html = _generate_head(participants)
    
    for participant in participants:
        html += _generate_participant(participant)

    html += _generate_foot()
    return html
