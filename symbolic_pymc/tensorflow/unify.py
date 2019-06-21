import tensorflow as tf

from kanren.term import term, operator, arguments

from unification.core import _reify, _unify, reify

from ..meta import metatize
from ..unify import ExpressionTuple, unify_MetaSymbol, tuple_expression
from .meta import TFlowMetaSymbol

tf_class_abstractions = tuple(c.base for c in TFlowMetaSymbol.__subclasses__())

_unify.add(
    (TFlowMetaSymbol, tf_class_abstractions, dict),
    lambda u, v, s: unify_MetaSymbol(u, metatize(v), s),
)
_unify.add(
    (tf_class_abstractions, TFlowMetaSymbol, dict),
    lambda u, v, s: unify_MetaSymbol(metatize(u), v, s),
)
_unify.add(
    (tf_class_abstractions, tf_class_abstractions, dict),
    lambda u, v, s: unify_MetaSymbol(metatize(u), metatize(v), s),
)


def _reify_TFlowClasses(o, s):
    meta_obj = metatize(o)
    return reify(meta_obj, s)


_reify.add((tf_class_abstractions, dict), _reify_TFlowClasses)

operator.add((tf.Tensor,), lambda x: operator(metatize(x)))

arguments.add((tf.Tensor,), lambda x: arguments(metatize(x)))

term.add((tf.Operation, ExpressionTuple), lambda op, args: term(metatize(op), args))

tuple_expression.add(tf_class_abstractions,
                     lambda x, shallow=False: tuple_expression(metatize(x), shallow))

__all__ = []
