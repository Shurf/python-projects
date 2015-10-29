# -*- coding: utf-8 -*-
import datetime
import codecs
from confluence import *

from suds.client import Client

from settings import *


class StatusLabels:
    Critical = 'Критично:'
    Important = 'Важно:'
    Resolved = 'Резолвы:'
    Closed = 'Закрыто:'


class Status:
    Reopen = unicode('reopen')
    New = unicode('new')
    Assigned = unicode('assigned')
    Resolved = unicode('resolved')
    Acknowledged = unicode('acknowledged')
    Closed = unicode('closed')


class CustomSort:
    MaxValue = 255
    Status = {
        Status.Reopen: 0,
        Status.New: 1,
        Status.Assigned: 2,
        Status.Resolved: 3,
        Status.Acknowledged: 4,
        Status.Closed: 5}

    @staticmethod
    def sort_by_status(status):
        if not status in CustomSort.Status.keys():
            return CustomSort.MaxValue
        return CustomSort.Status[status]


class BugType:
    Critical, Important, Resolved, Closed = range(4)


class Bug:
    def __init__(self, id=0, date_submitted=datetime.date.today, last_updated=datetime.date.today, summary=u"",
                 status=u""):
        self.id = id
        self.date_submitted = date_submitted
        self.last_updated = last_updated
        self.summary = summary
        self.status = status


class Project:
    def __init__(self, name=u""):
        self.name = name
        self.critical_bugs = {}
        self.important_bugs = {}
        self.resolved_bugs = {}
        self.closed_bugs = {}

    def add_bug(self, bug_from_mantis, type):

        bug_status = unicode(bug_from_mantis['status']['name'])
        if bug_status == Status.Closed:
            dict = self.closed_bugs
        elif bug_status == Status.Resolved:
            dict = self.resolved_bugs
        else:
            if type == BugType.Critical:
                dict = self.critical_bugs
            elif type == BugType.Important:
                dict = self.important_bugs
            else:
                raise ValueError("Unknown bug type")

        id = bug_from_mantis['id']
        if id in dict.keys():
            return

        dict[id] = Bug(
            id,
            bug_from_mantis['date_submitted'],
            bug_from_mantis['last_updated'],
            bug_from_mantis['summary'],
            bug_from_mantis['status']['name'])


class BugWorker:
    def __init__(self):
        self.client = Client(bugtracker_wsdl_url)
        self.projects = {}
        self.datetimenow = datetime.datetime.now()

    def add_bugs_from_id_array(self, id_array, type):
        for id in id_array:
            bug = self.client.service.mc_issue_get(bugtracker_login, bugtracker_password, id.strip())
            id = bug['project'].id
            if not id in self.projects.keys():
                self.projects[id] = Project(bug['project'].name)
            self.projects[id].add_bug(bug, type)

    def wrap_parameter_group(self, parameter_group):
        # return u"<tr>" + parameter_group + u"</tr>\n"
        return u"<li>" + parameter_group + u"</li>"

    def wrap_parameter(self, parameter):
        # return u"<td>" + parameter + u"</td>"
        return parameter

    def make_bug_date_parameter(self, bug_date):
        output = u""
        if (self.datetimenow - datetime.datetime.combine(bug_date.date(),
                                                         datetime.time())).days <= critical_dates_difference:
            output += u"<span style=\"color: rgb(255,0,0);\">(" + bug_date.strftime("%d.%m.%Y").encode(
                'utf-8') + u")</span> "
        return self.wrap_parameter(output)

    def make_summary_parameter(self, summary):
        return self.wrap_parameter(summary)

    def make_bug_id_parameter(self, bug_id):
        text_id = u"%07d" % bug_id
        output = u" (<a href=\"" + bug_url_prefix.encode('utf-8') + text_id + u"\">" + text_id + u"</a>)"
        return self.wrap_parameter(output)

    def make_bug_status_parameter(self, status):
        return u" [" + self.wrap_parameter(status) + u"]"

    def make_bug_entry(self, bug, show_status=False):
        output = u""
        output += self.make_bug_date_parameter(bug.date_submitted)
        output += self.make_summary_parameter(unicode(bug.summary))
        output += self.make_bug_id_parameter(bug.id)
        if show_status:
            output += self.make_bug_status_parameter(bug.status.encode('utf-8'))
        return self.wrap_parameter_group(output)

    def prepare_bug_list_output(self, bug_list, expandable=False, show_status=False):
        output = u""
        if expandable:
            output += u'<ac:rich-text-body>'
        output += u"<ul>"
        if not bug_list:
            output += self.wrap_parameter_group(u"---")
        else:
            for bug in sorted(bug_list,
                              key=lambda b: (
                                      CustomSort.sort_by_status(unicode(b.status)),
                                      -(self.datetimenow - b.date_submitted))):
                output += self.make_bug_entry(bug, show_status)
        output += u"</ul>"
        if expandable:
            output += u'</ac:rich-text-body>'
        return output

    def make_category_header(self, header, expandable=False):
        output = u""
        # output += u"<td colspan=4><h2>" + unicode(header) + u"</h2></td>"
        if expandable:
            output += u'<ac:parameter ac:name="title">'
        else:
            output += u"<p><strong>"
        output += header.decode('utf-8')
        if expandable:
            output += u'</ac:parameter>'
        else:
            output += u"</strong></p>"
        return output
        # return self.wrap_parameter_group(output)

    def make_project_header(self, header):
        output = u""
        # output += u"<td colspan=4><h1>" + unicode(header) + u"</h1></td>"

        output += u"<h2><span style=\"color: rgb(153,204,0);\">"
        output += unicode(header)
        output += u"</span></h2>"
        return output
        # return self.wrap_parameter_group(output)

    def make_category(self, header, items, expandable=False, show_status=False):
        output = u""
        if expandable:
            output += u'<p><br /></p>'
            output += u'<ac:structured-macro ac:name="expand">'
        output += self.make_category_header(header, expandable)
        output += self.prepare_bug_list_output(items, expandable, show_status)
        if expandable:
            output += u'</ac:structured-macro>'
        return output

    def make_document_body(self):
        output = u""
        for project_id in sorted(self.projects.keys()):
            project = self.projects[project_id]
            if not project.critical_bugs and not project.important_bugs:
                continue
            output += self.make_project_header(unicode(project.name))

            output += self.make_category(StatusLabels.Critical, project.critical_bugs.values(), False, True)
            output += self.make_category(StatusLabels.Important, project.important_bugs.values(), False, True)
            output += self.make_category(StatusLabels.Resolved, project.resolved_bugs.values())
            output += self.make_category(StatusLabels.Closed, project.closed_bugs.values(), True)

        return output

    def make_document(self):
        output = u""
        # output += u'<html>\n<head><meta charset="UTF-8"></head>\n<body>\n<table>\n'

        output += self.make_document_body()

        # output += u"</table>\n"
        # output += u"</body>"
        return output

    def prepare_output(self):
        return self.make_document()


bug_worker = BugWorker()
with open("critical_bugs.txt") as f:
    bug_worker.add_bugs_from_id_array(f.readlines(), BugType.Critical)

with open("important_bugs.txt") as f:
    bug_worker.add_bugs_from_id_array(f.readlines(), BugType.Important)

output = bug_worker.prepare_output()
with codecs.open(temporary_output_file_name, "wb", encoding='utf-8') as f:
    f.write(output)

cmd_line_args = []
cmd_line_args.append('-w')
cmd_line_args.append(wiki_url)
cmd_line_args.append('-u')
cmd_line_args.append(wiki_user)
cmd_line_args.append('-p')
cmd_line_args.append(wiki_password)
cmd_line_args.append('updatepage')
cmd_line_args.append('-f')
cmd_line_args.append(temporary_output_file_name)
cmd_line_args.append('-n')
cmd_line_args.append(wiki_page_name)
cmd_line_args.append('-s')
cmd_line_args.append(wiki_space)
args = Parser(cmd_line_args)

if args.verbose:
    console_handler.setLevel(logging.DEBUG)

content = Content(args)
server = Connect(args)
Actions(server["token"], server["xml_server"], args, content)

print "finished!"
