from openerp import models, fields


class ObjectClass(models.Model):
    _name = 'object.class'

    name = fields.Char('Class ID')
    subject_id = fields.Many2one('object.subject')
    number_credit = fields.Integer('Number of Credit')
    infor = fields.Char('Information')
    classroom = fields.Many2one('object.classroom', 'Classroom')
    lecturer = fields.Many2one('object.student.lecturer', 'Lecturer')
    date_start = fields.Date('Date Start')
    date_end = fields.Date('Date End')
