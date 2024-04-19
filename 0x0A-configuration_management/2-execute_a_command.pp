# Kills a process killmenow
exec { 'killmenow':
  command => 'pkill -9 killmenow',
  path    => '/usr/bin/'
}
