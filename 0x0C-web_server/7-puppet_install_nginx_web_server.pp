# Setting up Nginx using PUPPET

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure the default HTML page
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure redirection for /redirect_me
nginx::resource::vhost { 'default':
  ensure       => present,
  rewrite_to   => 'https://github.com/luischaparroc',
  rewrite_from => '^/redirect_me',
  require      => Package['nginx'],
}
