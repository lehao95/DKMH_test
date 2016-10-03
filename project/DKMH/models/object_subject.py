from openerp import models, fields


class ObjectSubject(models.Model):
    _name = 'object.subject'

    name = fields.Char('Subject Name')
    subject_id = fields.Char('Subject ID')
    number_credits = fields.Integer('Number of Credits')
    faculty_id = fields.Many2one('object.faculty', 'Faculty')
    subject_categories = fields.Selection([
        ('compulsory', 'Compulsory'),
        ('optional', 'Optional')
    ])

