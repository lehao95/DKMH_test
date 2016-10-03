from openerp import models, fields

class ObjectSemester(models.Model):
    _name = 'object.semester'

    name = fields.Char('Semester Name', required=True)
    line_semester_ids = fields.One2many('object.semester.line', 'name', 'Subjects')

