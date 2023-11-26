# Manage SSH client configuration to disable password authentication

exec { 'update_ssh_config':
  path    => '/usr/bin:/bin',
  command => 'echo -e "\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" ' \
             '>> /etc/ssh/ssh_config',
  unless  => 'grep -E "^\s*IdentityFile\s+~/.ssh/school" /etc/ssh/ssh_config && ' \
             'grep -E "^\s*PasswordAuthentication\s+no" /etc/ssh/ssh_config',
  require => File['/etc/ssh/ssh_config'],
}
