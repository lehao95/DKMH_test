from openerp import models, fields

class ObjectEducationProgram(models.Model):
    _name = 'object.education.program'

    name = fields.Char('Education Program Name')
    faculty_id = fields.Many2one('object.faculty', 'Faculty')
    course_id = fields.Many2one('object.course', 'Course')
    semester_ids = fields.One2many('object.semester', 'name', 'Semester')
