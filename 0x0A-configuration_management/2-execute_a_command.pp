# manifest that kills a process named killmenow

# exec resouce is used to execute a command
exec { 'killmenow':
  command => 'pkill -f killmenow', # parameter of exec: to be executed
  path    => ['/usr/bin', '/bin'], # search path for the command
}
