#changes SSH config file
exec { '/root/.ssh/config':
  command => '/usr/bin/cat ./2-ssh_config > /root/.ssh/config',
}
