=======================
 README Parallel Error
=======================

We want a Parallel task to wrap two functions.  If either one of them
raises an UserException, we should trap it OUTSIDE of the Parallel
task and send it to a Failed terminal state. If they both succeed, we
go to a Happy terminal state.
