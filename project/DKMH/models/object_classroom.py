from openerp import models, fields


class ObjectClassroom(models.Model):
    _name = 'object.classroom'

    name = fields.Char('Classroom Name')

