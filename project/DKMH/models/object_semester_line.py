from openerp import models, fields

class ObjectSubjectLine(models.Model):
    _name = 'object.semester.line'

    name = fields.Many2one('object.semester', 'Semester')
    subject_id = fields.Many2one('object.subject', 'Subject')
    number_credits = fields.Integer('Number of Credits')
    faculty_id = fields.Many2one('object.faculty', 'Faculty')
    subject_categories = fields.Selection([
        ('compulsory', 'Compulsory'),
        ('optional', 'Optional')
    ])



