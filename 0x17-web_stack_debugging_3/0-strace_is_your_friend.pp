# using strace, figuring what's causing 500 error returned by APACHE

exec { 'fix_apache_configuration':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => shell,
  notify   => Service['apache2']
}

# restarting apache after configuration
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix_apache_configuration']
}
