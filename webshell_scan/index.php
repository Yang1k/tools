<!DOCTYPE html>
<html class="no-js" lang="en">
<!--<![endif]-->

<head>
	<meta charset="UTF-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<title>shellscan</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="description" content="" />
	<meta name="keywords" content="" />
	<meta name="author" content="Your name" />
	<link rel="shortcut icon" href="./favicon.ico">
	<link rel="stylesheet" href="css/style1.css">
	<link rel="stylesheet" type="text/css" href="css/demo.css" />
	<link rel="stylesheet" type="text/css" href="css/style.css" />
	<link rel='stylesheet' href='./css/icon.css'>
	<link rel="stylesheet" type="text/css" href="css/materialize.min.css" />

	<script src="./js/prefixfree.min.js"></script>
</head>

<body>


	<!-- Home -->
	<div id="home" class="content">
		<h2><b>Webshell查杀工具</b></h2>
		<p>瞎写的
		</p>
	</div>
	<!-- /Home -->

	<!-- upload -->
	<div id="about" class="panel">
		<div class="content">
			<h2><b>上传源码</b></h2>

			<div class="row">
				<div class="col s12 offset-s2">
					<!-- Uploader Dropzone -->
					<form action="upload.php" id="zdrop" class="fileuploader center-align" style="margin-top:12%">
						<div id="upload-label" style="width: 200px;">
							<i class="material-icons">cloud_upload</i>
						</div>
						<span class="tittle">点击此处上传压缩包，目前仅支持zip格式的压缩包</span>
					</form>

					<!-- Preview collection of uploaded documents -->
					<div class="preview-container">
						<div class="collection card" id="previews">
							<div class="collection-item clearhack valign-wrapper item-template" id="zdrop-template">
								<div class="left pv zdrop-info" data-dz-thumbnail>
									<div>
										<span data-dz-name></span> <span data-dz-size></span>
									</div>
									<div class="progress">
										<div class="determinate" style="width:0" data-dz-uploadprogress></div>
									</div>
									<div class="dz-error-message"><span data-dz-errormessage></span></div>
								</div>

								<div class="secondary-content actions">
									<a href="#!" data-dz-remove
										class="btn-floating ph red white-text waves-effect waves-light"><i
											class="material-icons white-text">clear</i></a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="row" style="padding-top:3%">
				<div class="col s4 offset-s7">
					<a class="waves-effect waves-light btn" href="./scan.php" onclick="load()"><i
							class="material-icons right">send</i>扫描</a>

				</div>

			</div>
			<div class="indeterminate"></div>
		</div>
		<div class="" id="load"></div>
	</div>

	</div>
	<!-- upload -->

	<!-- result -->
	<?php
	error_reporting(0);
	session_start();
		$con = mysqli_connect("localhost:3306","root","root","scan");
		if (!$con) { 
			die("连接错误: " . mysqli_connect_error()); 
		} 
		$name = addslashes(pathinfo($_SESSION['filename'])['filename']);
		$time = addslashes($_SESSION['time']);
		$sql = "select * from scan_table where project='$name' and time>$time";
		$row = mysqli_query($con,$sql);
		$arr = array();
		while ($a = mysqli_fetch_assoc($row)) {
			$arr[]= $a;
		}
	?>
	<div id="contact" class="panel">
		<div class="content">
			<h2><b>扫描结果</b></h2>
			<?php 
				if (!empty($name) && empty($arr)) {
					?>
					<center>
					<h5 style="text-center">源码无异常</h5>
					</center>
				<?php
				}else{ ?>

			<table>
				<thead>
					<tr>
						<th data-field="id">编号</th>
						<th data-field="name" class="center">文件</th>
						<th data-field="price">代码</th>
					</tr>
				</thead>
				<tbody>

					<div class="row">
						<?php foreach ($arr as $key => $value) {?>
						<tr>
								<td><?php echo $value['id']; ?></td>
								<td><?php echo $value['filepath']; ?></td>
								<td><?php echo htmlentities($value['code']); ?></td>
						</tr>
						<?php }?>
					</div>

				</tbody>
			</table>
			<?php
				}			
			?>

		</div>
	</div>
	<!-- result -->

	<!-- Header with Navigation -->
	<div id="header">
		<span><b>----</b></span>
		<ul id="navigation">
			<li><a id="link-home" href="#home"><b>主页</b></a></li>
			<li><a id="link-about" href="#about"><b>上传源码</b></a></li>
			<li><a id="link-contact" href="#contact"><b>扫描结果</b></a></li>
		</ul>
		<!-- Demo Nav -->

	</span>
	<script src='./js/jquery-2.1.1.min.js'></script>
	<script src='./js/materialize.min.js'></script>
	<script src='./js/dropzone.js'></script>
	<script src="js/index.js"></script>
	<script>
		function load() {
			var arr = document.getElementById('load');
			arr.classList.add('loader');

			// loader active
		}
		// load()
	</script>

</body>

</html>